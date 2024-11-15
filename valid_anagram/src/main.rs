use::std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut hash_map: HashMap<char, u32> = HashMap::new();
        for c in s.chars() {
            match hash_map.get_mut(&c) {
                Some(value) => {*value += 1},
                None => {hash_map.insert(c, 1);}
            }
        }

        for c in t.chars() {
            match hash_map.get_mut(&c) {
                Some(value) => {
                    if *value == 0 {
                        return false
                    }
                    *value -= 1;
                },
                None => {
                    return false
                }
            }
        }

        for value in hash_map.into_values() {
            if value != 0 {
                return false;
            }
        }

        return true;
    }
}
fn main() {
    println!("{}", Solution::is_anagram(String::from("rat"), String::from("car")));
}
