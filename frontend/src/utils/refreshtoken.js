function RefreshToken() {
  const refresh = localStorage.getItem("refresh");
  return fetch("http://localhost:8000/api/token/refresh", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ refresh: refresh }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.detail === "Given token not valid for any token type") {
        localStorage.removeItem("refresh");
        localStorage.removeItem("token");
        return { message: "Expired token" };
      }
      localStorage.setItem("token", data.access);
    })
    .catch((err) => {
      console.log(err);
    });
}

export default RefreshToken;
