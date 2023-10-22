import React, {useState} from "react";
import "./LoginForm.css";
import {sha256} from "js-sha256";

function LoginForm({onClose}) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        const hashedPassword = sha256(password);
        fetch("http://localhost:8000/api/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password: hashedPassword }),
        })
        .then((res) => res.json())
        .then((data) => {
            console.log(data);
            onClose();
        })
        .catch((err) => {
            console.log(err);
        });
    }

    return (
    <div className="LoginForm-overlay">
      <div className="LoginForm">
        <button className="LoginForm-close" onClick={onClose}>
          X
        </button>
        <form onSubmit={handleSubmit}>
          <label>
            Username:
            <input type="text" name="username" value={username} onChange={(e) => setUsername(e.target.value)}/>
          </label>
          <label>
            Password:
            <input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)}/>
          </label>
          <input type="submit" value="Submit" />
        </form>
      </div>
    </div>
  );
}

export default LoginForm;