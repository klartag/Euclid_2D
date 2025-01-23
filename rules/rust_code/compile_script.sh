# A small script to compile the Linear-B library for the current Python version.
# The script should be called from the project root directory, using `rust_code/compile_script.sh`

cd rust_code
cargo build --release
cp target/release/liblinear_b.so ../linear_b.so