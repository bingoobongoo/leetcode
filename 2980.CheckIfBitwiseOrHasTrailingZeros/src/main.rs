struct Solution {}

impl Solution {
    pub fn has_trailing_zeros(nums: Vec<i32>) -> bool {
        let mut even_counter = 0;
        for num in nums {
            if num % 2 == 0 {
                even_counter += 1;
            }
            if even_counter >= 2 {
                return true;
            }
        }

        return false;
    }
}

fn main() {
    println!("{}", Solution::has_trailing_zeros([1, 2, 10].to_vec()));
}
