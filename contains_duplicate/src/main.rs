use::std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut hash_map: HashMap<i32, u32> = HashMap::new();
        for num in nums {
            match hash_map.get(&num) {
                Some(value) => {return true},
                None => {hash_map.insert(num, 1);}
            }
        }
        return false
    }
}

fn main() {
    println!("{}", Solution::contains_duplicate(Vec::from([1,1,1,1,1, 2, 3, 4])));
}