import RefreshToken from "./refreshtoken";

function LoadWorld(id, category) {
  const token = localStorage.getItem("token");
  return fetch("http://localhost:8000/api/worlds", {
      method: "POST",
      headers: {
      "Content-Type": "application/json",
      Authorization: `JWT ${token}`,
    },
      body: JSON.stringify({ request: "world", id: id, category: category }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.message === "Invalid token" || data.code === "token_not_valid") {
        RefreshToken();
        LoadWorld(id);
      } else {
        const world = JSON.parse(data);
        return world;
      }
    })
    .catch((err) => {
      console.log(err);
    });
}

export default LoadWorld;