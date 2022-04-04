use std::mem::replace;

use thiserror::Error;

//use num_bigint::BigInt;

/// MetalErrorPlus enumerates all possible errors
/// returned by this library.
/// Based on https://nick.groenen.me/posts/rust-error-handling/#the-library-error-type
#[derive(Error, Debug)]
pub enum MetalErrorPlus {
    #[error(transparent)]
    IOError(#[from] std::io::Error),

    #[error(transparent)]
    MetalError(#[from] MetalError),
}

#[derive(Error, Debug, Clone)]
pub enum MetalError {
    #[error("Raise Runtime Error: '{0}'")]
    RuntimeError(String),
}


fn fib(n: u32) -> usize {
    let mut f0: usize = 1;
    let mut f1: usize = 0;
    for _ in 0..n {
        let f2 = f0 + &f1;
        // This is a low cost way of swapping f0 with f1 and f1 with f2.
        f0 = replace(&mut f1, f2);
    }
    return f0;
}

fn busy_fib() {
    for _ in 0..10000 {
        for n in 0..42 {
            fib(n);
        }
    }
}


fn hello_rust(input_text: &str) {
    println!("hello from rust: {}", input_text);
}

fn error_rust() -> Result<(), MetalErrorPlus> {
    return Err(
        MetalError::RuntimeError("Test Exception".to_string()).into()
    );
}


mod python_module;
mod tests;
