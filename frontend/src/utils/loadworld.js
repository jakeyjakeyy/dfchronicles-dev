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
        const cleanedWorld = removeEmpty(world);
        return cleanedWorld;
      }
    })
    .catch((err) => {
      console.log(err);
    });
}

function removeEmpty(obj) {
  for (const key in obj) {
    if (obj[key] === null || obj[key] === undefined) {
      // Remove key if value is null or empty
      delete obj[key];
    } else if (typeof obj[key] === "object") {
      // Call for all nested objects
      removeEmpty(obj[key]);
    }
  }
  return obj;
}

export default LoadWorld;