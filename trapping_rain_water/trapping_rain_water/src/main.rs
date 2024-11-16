struct Solution {}

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = height.len() - 1;
        let mut trapped_water = 0;
        let mut current_height = 1;

        while left < right {
            while height[left] < current_height && left < right {
                left += 1;
            }
            while height[right] < current_height && left < right {
                right -= 1;
            }
            for i in left..right {
                if height[i] < current_height {
                    trapped_water += 1;
                }
            }
            current_height += 1;
        }
        return trapped_water;
    }
}

fn main() {
    println!("{}", Solution::trap(Vec::from([0,1,0,2,1,0,1,3,2,1,2,1])))
}
