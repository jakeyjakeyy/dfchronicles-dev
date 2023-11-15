import RefreshToken from "./refreshtoken";

global.fetch = jest.fn();

beforeEach(() => {
  fetch.mockClear();
  localStorage.clear();
});

test("RefreshToken handles token refresh correctly", async () => {
  const mockToken = "mockToken";
  localStorage.setItem("refresh", mockToken);

  const mockResponse = new Response(JSON.stringify({ access: "newToken" }));
  fetch.mockResolvedValueOnce(mockResponse);

  await RefreshToken();

  expect(localStorage.getItem("token")).toBe("newToken");
});
