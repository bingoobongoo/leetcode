struct Solution {}
impl Solution {
    pub fn check_string(s: String) -> bool {
        let mut noticedB = false;
        for char in s.chars() {
            if char == 'b' {
                noticedB = true;
            }
            if char == 'a' && noticedB {
                return false;
            }
        }
        return true;
    }
}

fn main() {}
