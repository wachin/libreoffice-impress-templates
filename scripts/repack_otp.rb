#!/usr/bin/ruby -KuU
# encoding: utf-8

require 'fileutils'

def build_otp(dir)
  otp = File.basename(dir) + ".otp"
  out = File.expand_path("../#{otp}", dir)

  Dir.chdir(dir) do
    FileUtils.rm_f(out)

    # ODF/OTP requires the mimetype file to be the first entry and uncompressed.
    system("zip", "-X0", out, "mimetype") or abort "Failed to add mimetype for #{otp}"

    entries = Dir.glob("*", File::FNM_DOTMATCH).reject do |entry|
      [".", "..", "mimetype"].include?(entry) || entry.end_with?(".md")
    end.sort

    unless entries.empty?
      system("zip", "-Xr9D", out, *entries) or abort "Failed to add content for #{otp}"
    end
  end

  puts "  * Template \"#{otp}\" built successfully"
end

# build individual templates
if ARGV[0]
  templates = ARGV
  templates.each do |d|
    build_otp(d)
  end
  exit
end

# build all templates
dirs = Dir.glob('*').select {|f| File.directory? f}

dirs.each do |d|
  build_otp(d)
end
