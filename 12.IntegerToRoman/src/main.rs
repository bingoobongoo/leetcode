fn to_roman(num: i32) -> char {
    match num {
        1000 => 'M',
        500 => 'D',
        100 => 'C',
        50 => 'L',
        10 => 'X',
        5 => 'V',
        1 => 'I',
        _ => panic!(),
    }
}

fn int_to_roman(num: i32) -> String {
    let mut answer: String = String::from("");
    let mut integer: i32 = num;
    let mut i: i32 = 1000;

    loop {
        if integer == 0 {
            break;
        }

        let letter: char = to_roman(i);
        let whole: i32 = integer / i;

        if whole == 0 {
            i /= 10;
            continue;
        } else if whole <= 3 {
            let tmp_str: String = String::from(letter.to_string().repeat(whole as usize));
            integer -= whole * i;
            answer.push_str(&tmp_str);
        } else if whole == 4 {
            let tmp_letter: char = to_roman(i * 5);
            integer -= i * 4;
            answer.push(letter);
            answer.push(tmp_letter);
        } else if whole <= 8 {
            let tmp_letter: char = to_roman(i * 5);
            integer -= i * 5;
            answer.push(tmp_letter);

            let whole: i32 = integer / i;
            let tmp_str: String = String::from(letter.to_string().repeat(whole as usize));
            integer -= whole * i;
            answer.push_str(&tmp_str);
        } else {
            let tmp_letter: char = to_roman(i * 10);
            integer -= i * 9;
            answer.push(letter);
            answer.push(tmp_letter);
        }

        i /= 10;
    }

    return answer;
}

fn main() {
    println!("{}", int_to_roman(1000));
}
