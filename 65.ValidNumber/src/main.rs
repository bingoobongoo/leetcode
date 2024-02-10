struct Solution {}
impl Solution {
    pub fn is_number(s: String) -> bool {
        let str = s;
        if Self::is_integer(str.clone()) || Self::is_decimal(str.clone()) {
            return true;
        }

        let e_index = str.find(['e', 'E']);
        let e_int_index: usize = match e_index {
            Some(index) => index,
            None => 0 as usize,
        };
        if e_int_index == 0 {
            return false;
        } else {
            let left_string = &str[0..e_int_index];
            let right_string = &str[e_int_index + 1..];
            if Self::is_integer(String::from(left_string))
                || Self::is_decimal(String::from(left_string))
            {
                if Self::is_integer(String::from(right_string)) {
                    return true;
                }
            }
        }

        return false;
    }

    pub fn is_integer(s: String) -> bool {
        let str = s;
        let mut start_idx = 0;
        if str.is_empty() {
            return false;
        }

        match &str[0..1] {
            "-" => {
                start_idx = 1;
            }
            "+" => {
                start_idx = 1;
            }
            _ => (),
        };

        if start_idx == str.len() {
            return false;
        }

        for char in str[start_idx..].chars() {
            if char.is_numeric() == false {
                return false;
            }
        }
        return true;
    }

    pub fn is_decimal(s: String) -> bool {
        let str = s;
        let mut dot = false;
        let mut has_digit = false;
        let mut start_idx = 0;
        if str.is_empty() {
            return false;
        }

        match &str[0..1] {
            "-" => {
                start_idx = 1;
            }
            "+" => {
                start_idx = 1;
            }
            _ => (),
        };

        if str.len() == 1 {
            // either an integer or not a number
            return false;
        }

        for char in str[start_idx..].chars() {
            if char.is_numeric() == false {
                if char == '.' {
                    if dot {
                        return false;
                    }
                    dot = true;
                } else {
                    return false;
                }
            } else {
                has_digit = true;
            }
        }

        if !dot || !has_digit {
            // decimal must have '.' character and at least one digit according to definition
            return false;
        }

        return true;
    }
}

fn main() {
    let s = String::from("+.");
    println!("{}", Solution::is_number(s))
}
