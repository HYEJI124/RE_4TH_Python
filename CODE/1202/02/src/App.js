import logo from "./logo.svg";
import "./App.css";

function App() {
  const profile = {
    name: "김철수",
    age: 28,
    job: "프론트엔드 개발자",
    skills: ["JavaScript", "React", "TypeScript", "CSS"],
    image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSR0IRHHF2HPjGS2nLFWwleD9D4odICtycZgA&s",
  };

  return (
    <div className="card">
      <img src={profile.image} alt="profile" className="profile-image" />

      <h2>{profile.name}</h2>
      <p>나이: {profile.age}</p>
      <p>직업: {profile.job}</p>

      <h3>보유 기술</h3>
      <ul>
        {profile.skills.map((skill) => (
          <li key={skill}>{skill}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
