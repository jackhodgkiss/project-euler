fn get_factors(number: u64) -> Vec<u64> {
    let mut factors = vec![1, number];
    for element in (2u64..).take_while(|x| x * x <= number + 1) {
        if number % element == 0 {
            insert_factor(&mut factors, element);
            insert_factor(&mut factors, number / element);
        }
    }
    fn insert_factor(factors: &mut Vec<u64>, factor: u64) -> () {
        match factors.binary_search(&factor) {
            Ok(_position) => {}
            Err(position) => factors.insert(position, factor),
        }
    }
    factors
}

fn main() {
    let number: u64 = 600_851_475_143;
    let answer: u64 = get_factors(number)
        .into_iter()
        .rfind(|x| get_factors(*x).len() == 2)
        .unwrap();
    println!("Answer: {}", answer);
}
