fn main() {
    let answer: u32 = (3u32..1_000u32)
        .filter(|number: &u32| number % 3 == 0 || number % 5 == 0)
        .sum();
    println!("Answer: {}", answer);
}
