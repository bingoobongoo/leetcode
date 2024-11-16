struct Solution {}

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let mut nums1 = nums1;
        let mut nums2 = nums2;
        let mut vec_sum: Vec<i32> = Vec::new();
        while !(nums1.is_empty() && nums2.is_empty()){
            if nums1.is_empty() {
                vec_sum.push(*nums2.first().unwrap());
                nums2.remove(0);
            }
            else if nums2.is_empty() {
                vec_sum.push(*nums1.first().unwrap());
                nums1.remove(0);
            }
            else if nums1.first().unwrap() >= nums2.first().unwrap() {
                vec_sum.push(*nums2.first().unwrap());
                nums2.remove(0);                
            }
            else {
                vec_sum.push(*nums1.first().unwrap());
                nums1.remove(0);
            }
        }
        let median: f64;
        if vec_sum.len() % 2 == 0 {
            let middle = vec_sum.len() / 2;
            median = (vec_sum[middle-1] + vec_sum[middle]) as f64 / 2.0;
        }
        else {
            let middle = vec_sum.len() / 2;
            median = vec_sum[middle] as f64;
        }

        return median;
    }
}

fn main() {
    println!("{}", Solution::find_median_sorted_arrays(Vec::from([1,2]), Vec::from([3])));
}
