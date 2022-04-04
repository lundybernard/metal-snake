// Rust translator founctions that can be called by Python
use pyo3::{
    exceptions::PyIOError,
    exceptions::PyRuntimeError,
    exceptions::PyValueError,
    prelude::{pymodule, PyModule, PyResult, Python},
    PyErr,
};

use crate::{
    fib,
    busy_fib,
    hello_rust,
    error_rust,
    MetalErrorPlus,
    MetalError,
};

//use num_bigint::BigInt;


#[pymodule]
#[pyo3(name = "rust")]
fn metal_snake_py(_py: Python<'_>, m:&PyModule) -> PyResult<()> {
    // ref: https://pyo3.rs/v0.15.1/module.html

    #[pyfn(m)]
    #[pyo3(name = "rfib")]
    fn rfib(n: u32) -> Result<usize, PyErr> {
        return Ok(fib(n));
    }

    #[pyfn(m)]
    #[pyo3(name = "busy_fib")]
    fn busy_fib_py() -> Result<(), PyErr> {
        busy_fib();
        return Ok(());
    }

    #[pyfn(m)]
    #[pyo3(name = "hello_rust")]
    fn hello_rust_py(input_text: &str) -> Result<(), PyErr> {
        hello_rust(input_text);
        return Ok(());
    }

    #[pyfn(m)]
    #[pyo3(name = "error_rust")]
    fn error_rust_py() -> Result<(), PyErr> {
        error_rust()?;
        Ok(())
    }


    /* implement a converter from BedErrorPlus to PyErr.
    The converter creates the right class of Python error
    (IOError, ValueError, or IndexError) with the right error message
    */
    mod io {
        pyo3::import_exception!(io, UnsupportedOperation);
    }

    impl std::convert::From<MetalErrorPlus> for PyErr {
        fn from(err: MetalErrorPlus) -> PyErr {
            match err {
                MetalErrorPlus::IOError(_) => {
                    PyIOError::new_err(err.to_string())
                }
                MetalErrorPlus::MetalError(MetalError::RuntimeError(_)) => {
                    PyRuntimeError::new_err(err.to_string())
                },
                _ => PyValueError::new_err(err.to_string()),
            }
        }
    }

    Ok(())
}
