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
  } else if (request === "favoriteQuery") {
    const token = localStorage.getItem("token");
    return fetch("http://localhost:8000/api/generations", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `JWT ${token}`,
      },
      body: JSON.stringify({
        request: "favorite",
        generation: id,
        query: "query",
      }),
    })
      .then((res) => res.json())
      .then(async (data) => {
        return HandleRefresh(data, request, id);
      })
      .catch((err) => {
        console.log(err);
        throw err;
      });
  } else if (request === "favorite") {
    const token = localStorage.getItem("token");
    return fetch("http://localhost:8000/api/generations", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `JWT ${token}`,
      },
      body: JSON.stringify({
        request: "favorite",
        generation: id,
      }),
    })
      .then((res) => res.json())
      .then(async (data) => {
        return HandleRefresh(data, request, id);
      })
      .catch((err) => {
        console.log(err);
        throw err;
      });
  }
}

async function HandleRefresh(data, request, id, feedback) {
  if (data.message === "Invalid token" || data.code === "token_not_valid") {
    const res = await RefreshToken();
    if (res && res.message === "Expired token") {
      return { message: "Please log in again." };
    }
    return Generations(request, id);
  } else {
    return data;
  }
}

export default Generations;
