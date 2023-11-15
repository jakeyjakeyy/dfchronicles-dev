import RefreshToken from "./refreshtoken";

async function Generations(request, id, feedback) {
  if (request === undefined) {
    return fetch("http://localhost:8000/api/generations", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        return data;
      })
      .catch((err) => {
        console.log(err);
        throw err;
      });
  }
}

export default Generations;
