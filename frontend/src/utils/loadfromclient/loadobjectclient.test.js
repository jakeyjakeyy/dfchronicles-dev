import fs from "fs";
import path from "path";
import loadObjectClient from "./loadobjectclient";
import XMLParser from "react-xml-parser";

const legends = fs.readFileSync(
  path.resolve(__dirname, "../../../tests/xml/region3-00100-01-01-legends.xml"),
  "utf8"
);
const legendsxml = new XMLParser().parseFromString(legends);

describe("loadObjectClient", () => {
  it("processes battleEventCol.json correctly", () => {
    const input = JSON.parse(
      fs.readFileSync(
        path.resolve(__dirname, "../../../tests/battleEventCol.json"),
        "utf8"
      )
    );
    const expectedOutput = JSON.parse(
      fs.readFileSync(
        path.resolve(__dirname, "../../../tests/battleEventColOutput.json"),
        "utf8"
      )
    );

    const result = loadObjectClient(input, {}, {});

    expect(result).toEqual(expectedOutput);
  });
});
