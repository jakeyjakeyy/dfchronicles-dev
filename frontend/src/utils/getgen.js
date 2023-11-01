import RefreshToken from "./refreshtoken";

function GetGen(object) {
  const token = localStorage.getItem("token");
  return fetch("http://localhost:8000/api/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `JWT ${token}`,
    },
    body: JSON.stringify({
      request: "generate",
      prompt: object,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.message === "Invalid token" || data.code === "token_not_valid") {
        RefreshToken();
        return GetGen(object);
      } else {
        const gen = JSON.parse(data);
        return gen;
      }
    })
    .catch((err) => {
      console.log(err);
    });
}

export default GetGen;
