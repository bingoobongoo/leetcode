fn dictionary(num: i32) -> String {
    match num {
        0 => String::from("Zero"),
        1 => String::from("One"),
        2 => String::from("Two"),
        3 => String::from("Three"),
        4 => String::from("Four"),
        5 => String::from("Five"),
        6 => String::from("Six"),
        7 => String::from("Seven"),
        8 => String::from("Eight"),
        9 => String::from("Nine"),
        10 => String::from("Ten"),
        11 => String::from("Eleven"),
        12 => String::from("Twelve"),
        13 => String::from("Thirteen"),
        14 => String::from("Fourteen"),
        15 => String::from("Fifteen"),
        16 => String::from("Sixteen"),
        17 => String::from("Seventeen"),
        18 => String::from("Eighteen"),
        19 => String::from("Nineteen"),
        20 => String::from("Twenty"),
        30 => String::from("Thirty"),
        40 => String::from("Forty"),
        50 => String::from("Fifty"),
        60 => String::from("Sixty"),
        70 => String::from("Seventy"),
        80 => String::from("Eighty"),
        90 => String::from("Ninety"),
        100 => String::from("Hundred"),
        1000 => String::from("Thousand"),
        1_000_000 => String::from("Million"),
        1_000_000_000 => String::from("Billion"),
        _ => String::from("-1"),
    }
}

fn number_to_words(num: i32) -> String {
    let mut divisor: i32 = 1_000_000_000;
    let mut number: i32 = num;
    let mut answer: String = String::from("");

    loop {
        if number == 0 && divisor == 1_000_000_000 {
            return dictionary(0);
        }

        if number == 0 {
            break;
        }

        let whole: i32 = number / divisor;
        if whole == 0 {
            if divisor <= 1000 {
                divisor /= 10
            } else {
                divisor /= 1000;
            }
            continue;
        }

        let remainder: i32 = number % divisor;

        if dictionary(number) != String::from("-1") {
            if divisor >= 100 {
                answer.push_str(&format!("{} ", &dictionary(whole)));
            }
            answer.push_str(&dictionary(number));
            break;
        } else if dictionary(whole) == String::from("-1") {
            answer.push_str(&format!("{} ", &number_to_words(whole)));
        } else if divisor == 10 {
            answer.push_str(&format!("{} ", &dictionary(whole * divisor)));
        } else {
            answer.push_str(&format!("{} ", &number_to_words(whole)));
        }

        if divisor >= 100 {
            answer.push_str(&format!("{} ", &dictionary(divisor)));
        }

        number = remainder;
    }

    answer = String::from(answer.trim());
    return answer;
}

fn main() {
    println!("{}", number_to_words(879666789));
}
