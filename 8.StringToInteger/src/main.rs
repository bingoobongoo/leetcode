struct Solution {}
impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let str = s.trim_start();
        let mut answer_str = String::from("");
        let mut answer_int = 0;
        let mut sign = false;
        let mut start_idx = 0;

        if str.is_empty() {
            return 0;
        }

        match &str[0..1] {
            "-" => {
                sign = true;
                start_idx = 1;
            }
            "+" => {
                start_idx = 1;
            }
            _ => (),
        }

        for char in str[start_idx..].chars() {
            if char.is_numeric() == false {
                break;
            }
            answer_str.push(char)
        }

        if answer_str.is_empty() {
            return answer_int;
        }

        answer_int = match answer_str.parse::<i32>() {
            Ok(num) => {
                if sign {
                    -num
                } else {
                    num
                }
            }

            Err(_) => {
                if sign {
                    i32::MIN
                } else {
                    i32::MAX
                }
            }
        };

        return answer_int;
    }
}

fn main() {
    let s = String::from("");
    println!("{}", Solution::my_atoi(s))
}
