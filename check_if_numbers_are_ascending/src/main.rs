struct Solution {}
impl Solution {
    pub fn are_numbers_ascending(s: String) -> bool {
        let mut counter = -1;
        let tokens: Vec<&str> = s.split(" ").collect();
        for token in tokens {
            match token.parse::<i32>() {
                Ok(num) => {
                    if num <= counter {
                        return false;
                    } else {
                        counter = num;
                    }
                }
                Err(_) => (),
            }
        }

        return true;
    }
}

fn main() {}
