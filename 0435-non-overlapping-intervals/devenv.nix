{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/packages/
  name = "leetcode";
  packages = [ pkgs.git pkgs.python311 ];
}
