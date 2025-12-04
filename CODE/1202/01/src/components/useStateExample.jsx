import { useState } from "react";

function UseStateExample() {
  const [count, setCount] = useState(0);

  const increase = () => {
    setCount((prev) => prev + 1);
  };

  const decrease = () => {
    setCount((prev) => prev - 1); // 감소
  };

  const reset = () => {
    setCount(0); // 초기화
  };

  const double = () => {
    setCount((prev) => prev * 2); // 2배
  };

  return (
    <div>
      <p>{count}</p>

      {/* 증가 */}
      <button onClick={increase}>증가</button>

      {/* 감소 */}
      <button onClick={decrease}>감소</button>

      {/* 초기화 */}
      <button onClick={reset}>초기화</button>

      {/* 2배 */}
      <button onClick={double}>2배 증가</button>
    </div>
  );
}

export default UseStateExample;
