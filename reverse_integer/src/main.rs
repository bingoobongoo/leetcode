struct Solution {}

impl Solution {
    pub fn reverse(mut x: i32) -> i32 {
        let sign = x < 0;
        x = x.abs();
        let str = x.to_string();
        let mut rev_string = String::from("");

        if sign {
            rev_string.push('-');
        }
        for char in str.chars().rev() {
            rev_string.push(char);
        }

        let answer = match rev_string.parse::<i32>() {
            Ok(num) => num,
            Err(_) => 0,
        };

        return answer;
    }
}

fn main() {
    println!("{}", Solution::reverse(1_980_002_378));
}
