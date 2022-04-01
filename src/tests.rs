#[cfg(test)]
mod tests {
    #[test]
    fn test_fib() {
        for &(x, y) in [
            (0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8),
        ].iter() {
            assert_eq!(fib(x), y);
        }
    }

    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
