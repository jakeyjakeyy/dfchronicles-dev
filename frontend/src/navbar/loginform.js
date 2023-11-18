import React, { useState } from "react";
import "./loginform.css";

function LoginForm({ onClose, register }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [password2, setPassword2] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (register === true) {
      if (password !== password2) {
        alert("Passwords do not match");
        return;
      }
      fetch("http://localhost:8000/api/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          request: "register",
          username: username,
          password: password,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          if (
            data.message === "User already exists" ||
            data.message === "Invalid username or password."
          ) {
            alert("User already exists");
            return;
          } else {
            localStorage.setItem("token", data.access);
            localStorage.setItem("refresh", data.refresh);
            localStorage.setItem("username", username);
            onClose();
            window.location.reload();
          }
        });
    } else {
      fetch("http://localhost:8000/api/token", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      })
        .then((res) => res.json())
        .then((data) => {
          if (
            data.detail === "No active account found with the given credentials"
          ) {
            alert("Invalid username or password.");
            return;
          }
          localStorage.setItem("token", data.access);
          localStorage.setItem("refresh", data.refresh);
          localStorage.setItem("username", username);
          onClose();
          window.location.reload();
        })
        .catch((err) => {
          console.log(err);
        });
    }
  };

  return (
    <div className="LoginForm-overlay">
      <div className="LoginForm">
        <button className="LoginForm-close" onClick={onClose}>
          X
        </button>
        <form onSubmit={handleSubmit}>
          <label>
            Username:
            <input
              type="text"
              name="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </label>
          <label>
            Password:
            <input
              type="password"
              name="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </label>
          {register && (
            <label>
              Confirm Password:
              <input
                type="password"
                name="password2"
                value={password2}
                onChange={(e) => setPassword2(e.target.value)}
              />
            </label>
          )}
          <input type="submit" value="Submit" />
        </form>
      </div>
    </div>
  );
}

export default LoginForm;
