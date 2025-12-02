// 과제 1: 나이 판별 프로그램

let age = 3;

if (age < 7) {
    console.log('미취학 아동');
} else if (age <= 13) {
    console.log('초등학생');
} else if (age <= 16) {
    console.log('중학생');
} else if (age <= 19) {
    console.log('고등학생');
} else {
    console.log('성인');
}

// 과제 2: 계절 판별
let month = 9;

switch(month){
    case 3:
    case 4:
    case 5:
        console.log('봄');
    case 6:
    case 7:
    case 8:
        console.log('여름');
        break
    case 9:
    case 10:
    case 11:
        console.log('가을');
        break
    case 12:
    case 1:
    case 2:
        console.log('겨울');
        break
}

// 과제 3: 윤년 계산
let year = 2025;

let result = (year % 4 === 0) && (year % 100 !== 0 || year % 400 === 0) ? '윤년':'평년'
console.log(result);


// 나이 판별 프로그램
let age15 = 15;

if (age15 < 7) {
    console.log('미취학 아동');
} else if (age15 >= 7 && age15 <= 13) {
    console.log('초등학생');
} else if (age15 >= 14 && age15 <= 16) {
    console.log('중학생');
} else if (age15 >= 17 && age15 <= 19) {
    console.log('고등학생');
} else {
    console.log('성인');
}

// 계절 판별
let month1 = 10;

if (month1 >= 3 && month1 <= 5) {
    console.log('봄');
} else if (month1 >= 6 && month1 <= 8) {
    console.log('여름');
} else if (month1 >= 9 && month1 <= 11) {
    console.log('가을');
} else if (month1 === 12 || month1 === 1 || month1 === 2) {
    console.log('겨울');
} else {
    console.log('잘못된 월입니다.');
}

// 윤년 계산
let year1 = 2024;

if ((year1 % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    console.log('윤년입니다.');
} else {
    console.log('윤년이 아닙니다.');
}