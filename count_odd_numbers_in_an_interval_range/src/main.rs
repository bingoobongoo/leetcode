struct Solution {}

impl Solution {
    pub fn count_odds(low: i32, high: i32) -> i32 {
        let mut odd_counter = 0;
        if high == low && high % 2 == 1 {return 1}
        else if high == low && high % 2 == 0 {return 0}

        if low % 2 == 1 || high % 2 == 1 {
            odd_counter += (high - low)/2 + 1
        } else {
            odd_counter += (high - low)/2
        }
        
        return odd_counter
    }
}

fn main() {
    println!("{}", Solution::count_odds(8, 10));
}
