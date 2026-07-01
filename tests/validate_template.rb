#!/usr/bin/env ruby
# frozen_string_literal: true

require 'pathname'
require 'rexml/document'

REQUIRED_XML = %w[
  content.xml
  styles.xml
  meta.xml
  settings.xml
  META-INF/manifest.xml
].freeze

REQUIRED_PACKAGE_ENTRIES = %w[
  mimetype
  content.xml
  styles.xml
  meta.xml
  settings.xml
  META-INF/manifest.xml
].freeze

EXPECTED_MIMETYPE = "application/vnd.oasis.opendocument.presentation-template"

def fail_with(message)
  warn "ERROR: #{message}"
  exit 1
end

def info(message)
  puts "OK: #{message}"
end

def parse_xml(path)
  File.open(path, "r:utf-8") do |file|
    REXML::Document.new(file)
  end
end

def validate_directory(dir)
  fail_with("No existe el directorio #{dir}") unless dir.directory?

  REQUIRED_XML.each do |relative|
    path = dir.join(relative)
    fail_with("Falta #{relative}") unless path.file?
    parse_xml(path)
    info("XML valido: #{relative}")
  end

  mimetype_path = dir.join("mimetype")
  fail_with("Falta mimetype") unless mimetype_path.file?

  mimetype = mimetype_path.read.strip
  fail_with("mimetype inesperado: #{mimetype}") unless mimetype == EXPECTED_MIMETYPE
  info("mimetype correcto")

  markdown_files = dir.glob("**/*.md").map { |path| path.relative_path_from(dir).to_s }.sort
  if markdown_files.empty?
    info("No hay archivos .md dentro de la plantilla")
  else
    fail_with("Hay archivos .md dentro de la plantilla: #{markdown_files.join(', ')}")
  end
end

def run_command(*command)
  output = `#{command.map { |part| "'#{part.to_s.gsub("'", %q('\\''))}'" }.join(' ')}`
  fail_with("Fallo al ejecutar: #{command.join(' ')}") unless $?.success?
  output
end

def validate_package(otp)
  fail_with("No existe el archivo #{otp}") unless otp.file?

  entries = run_command("unzip", "-Z1", otp.to_s).lines.map(&:strip)
  fail_with("El paquete esta vacio") if entries.empty?
  fail_with("La primera entrada no es mimetype") unless entries.first == "mimetype"

  REQUIRED_PACKAGE_ENTRIES.each do |entry|
    fail_with("Falta #{entry} dentro del .otp") unless entries.include?(entry)
  end
  info("Entradas ODF requeridas presentes en el .otp")

  listing = run_command("unzip", "-lv", otp.to_s)
  mimetype_line = listing.lines.find { |line| line.include?(" mimetype") }
  fail_with("No se pudo inspeccionar mimetype dentro del .otp") unless mimetype_line
  fail_with("mimetype fue comprimido dentro del .otp") unless mimetype_line.include?("Stored")
  info("mimetype va primero y sin compresion en el .otp")
end

input = ARGV[0] or fail_with("Uso: ruby tests/validate_template.rb RUTA_A_PLANTILLA")

dir = Pathname.new(input).expand_path
validate_directory(dir)

otp = dir.parent.join("#{dir.basename}.otp")
if otp.file?
  validate_package(otp)
else
  warn "WARN: No existe #{otp}, se valido solo la carpeta fuente"
end

puts "Plantilla validada: #{dir}"
