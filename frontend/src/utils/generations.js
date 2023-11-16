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
  if (request === "favoriteQuery") {
    return apiCall(request, {
      request: "favorite",
      generation: id,
      query: "query",
    });
  } else if (request === "favorite") {
    return apiCall(request, { request: "favorite", generation: id });
  } else if (request === "commentQuery") {
    return apiCall(request, {
      request: "comment",
      generation: id,
      query: "query",
    });
  } else if (request === "comment") {
    return apiCall(request, {
      request: "comment",
      generation: id,
      comment: feedback,
    });
  }
}

function apiCall(request, data) {
  const token = localStorage.getItem("token");
  return fetch("http://localhost:8000/api/generations", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `JWT ${token}`,
    },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then(async (res) => {
      return HandleRefresh(res, request, data.generation);
    })
    .catch((err) => {
      console.log(err);
      throw err;
    });
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
