# A small script to compile the Linear-B library for the current Python version.
# The script should be called from the project root directory, using `.\rust_code\compile_script.ps1`

cd rust_code
cargo build --release
copy-item .\target\release\linear_b.dll ../linear_b.pyd
cd ..