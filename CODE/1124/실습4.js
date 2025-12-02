// 과제 1: 온도 변환기
// 공식: 화씨 = 섭씨 x 9/5 + 32

console.log('과제 1');

function celsiusToFahrenheit(celsius) {
    return celsius * 9/5 + 32;
};

console.log(celsiusToFahrenheit(0));

// 과제 2: 배열 평균 구하기
console.log('과제 2');

function average(numbers) {
    let sum = 0;
    for (const num of numbers) {
        sum += num;
    }
    return sum / numbers.length;
}

console.log(average([10, 20, 30]));