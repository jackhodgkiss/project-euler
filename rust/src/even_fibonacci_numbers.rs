struct Fib {
    current: u32,
    next: u32,
}

impl Iterator for Fib {
    type Item = u32;
    fn next(&mut self) -> Option<Self::Item> {
        let iter_current = self.current;
        self.current = self.next;
        self.next += iter_current;
        Some(iter_current)
    }
}

fn fibonacci() -> Fib {
    Fib {
        current: 0,
        next: 1,
    }
}

fn main() {
    let answer: u32 = fibonacci()
        .take_while(|number| number < &4_000_000)
        .filter(|number| number % 2 == 0)
        .sum();
    println!("Answer: {}", answer);
}
