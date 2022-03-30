use thiserror::Error;

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
