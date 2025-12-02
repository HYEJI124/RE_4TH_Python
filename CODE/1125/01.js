// 재귀함수
// 함수가 자기 자신을 호출

const factorial = (n) => {
    // 재귀 함수 종료 조건
    if (n == 1) return 1;
    return n * factorial(n - 1);
};

console.log(factorial(5));

// 스코프(Scope)
// 변수의 유효 범위

// 어디서든 접근 가능
let globalVar = '전역변수';
function function1() {
    // 함수 내에서만 접근 가능
    let localVar = '지역변수';
    console.log(globalVar);
    console.log(localVar);
}

function1();

console.log(globalVar);
// console.log(localVar);

console.log();
console.log();
console.log();

// 콜백 함수
// 다른 함수의 인자로 전달되는 함수

function greet(name, callback) {
    console.log(`안녕하세요 ${name}님!`);
    callback();
}

function sayGoodbye() {
    console.log('안녕히 가세요!');
}

greet('홍길동', sayGoodbye);
console.log();

// 배열 메서드와 콜백
// 파이썬의 리스트와 비슷

let numbers = [1, 2, 3, 4, 5];
console.log(numbers[1]); // 2
console.log();

// 순회
numbers.forEach((num) => {
    console.log(num * 2);
});
console.log();

// filter
let evens = numbers.filter((num) => num % 2 === 0);
console.log(evens);
// let evens = numbers.filter((num) => {return num % 2 === 0});
console.log();

// map
let doubled = numbers.map(num => num * 2);
console.log(doubled);
console.log();
// map: 반환값 있음 // [ 2, 4, 6, 8, 10 ]

// forEach: 반환값 없음
const doubled1 = numbers.forEach((num) => {
    return console.log(num * 2);
});
console.log('doubled1', doubled1); //undefined

// 배열 추가 / 제거
// 끝에 추가
numbers.push(6);
console.log('numbers', numbers);
console.log();

// 끝에서 제거
numbers.pop();
console.log('numbers', numbers);
console.log();

// 앞에 추가
numbers.unshift(0);
console.log('numbers', numbers);
console.log();

// 앞에서 제거
numbers.shift(0);
console.log('numbers', numbers);
console.log();

// 검색
// indexOf: 인덱스 찾기
let fruits = ['사과', '바나나', '딸기', '포도']
console.log(fruits.indexOf('바나나'));
console.log(fruits.indexOf('딸기'));
console.log(fruits.indexOf('수박')); // -1
console.log();

// includes: 포함 여부
console.log(fruits.includes('딸기'));
console.log(fruits.includes('수박'));
console.log();

// 조작
// slice: 부분 복사(원본 유지)
let some = fruits.slice(1, 3);
console.log(some);
console.log(fruits);
console.log();

// splice: 추가/제거/교체(원본 변경)
fruits.splice(1, 1); // 인덱스 1부터 1개 제거
console.log(fruits);
console.log();

fruits.splice(1, 0, '오렌지'); // 인덱스 1에 삽입
console.log(fruits);
console.log();

// 변환
// join: 문자열로 변환
console.log(fruits.join()); // 기본 ','
console.log(fruits.join('-'));
console.log();

// concat: 배열 합치기
let more = fruits.concat(['수박', '복숭아']);
console.log(more);
console.log();

console.log('numbers', numbers);
// reverse: 순서 뒤집기
numbers.reverse();
console.log('numbers', numbers);
console.log();

more.reverse();
console.log('more', more);
console.log();

// 정렬
fruits.sort();
more.sort();
console.log('fruits', fruits);
console.log('more', more);
console.log();

let numbers1 = [10, 4, 2, 20];
// 0보다 작은 경우
// a를 b보다 낮은 색인(인덱스)으로 정렬
// a = 2, b = 20, a - b = -18 < 0

// 0보다 큰 경우
// b를 a보다 낮은 색인(인덱스)으로 정렬
// a = 10, b = 4, a - b = 6 > 0

numbers1.sort((a, b) => a - b); // 오름차순
console.log('numbers1', numbers1);
numbers1.sort((a, b) => b - a); // 내림차순
console.log('numbers1', numbers1);
console.log();

// 실습 1
let fruits1 = ['복숭아', '수박', '포도', '딸기', '오렌지'];

// for문 모든 요소 출력
console.log('===== 1 =====');

for (let i = 0; i < fruits1.length; i++) {
    console.log(fruits1[i]);
}
console.log();

// for .. of 모든 요소 출력
console.log('===== 2 =====');

for (let fruit of fruits1) {
    console.log(fruit);
}
console.log();


// forEach 모든 요소 출력
console.log('===== 3 =====');

fruits1.forEach((fruit) => {
    console.log(fruit);
});
console.log();

// 실습 2: 배열 조작
array = [3, 7, 2, 9, 5, 1, 8]

// 1. 5보다 큰 숫자만 필터링
array = array.filter((arr) => arr > 5);
console.log(array);
console.log();

// 2. 각 숫자를 제곱
array = array.map((arr) => arr ** 2);
console.log(array);
console.log();

// 3. 오름차순 정렬
array.sort()
console.log(array);
console.log();

// 배열 조작 - 리더님 풀이
const numbers2 = [3, 7, 2, 9, 5, 1, 8]

// 5보다 큰 숫자만 필터링
const arr1 = numbers2.filter((num) => num > 5);

// 각 숫자를 제곱
const arr2 = arr1.map((num) => num ** 2)

// 오름차순 정렬
arr2.sort();
console.log(arr2);

// 메소드체이닝
const arr = numbers2.filter((num) => num > 5).map((num) => num ** 2).sort();
console.log(arr);

console.log();
console.log();
console.log();

