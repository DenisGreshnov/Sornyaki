import React from "react";

import { TIFFViewer } from "react-tiff";
import "react-tiff/dist/index.css";
import tiffFile from "./multipage.tiff";

const App = () => {
  return (
    <TIFFViewer
      tiff={tiffFile}
      lang="en" // en | de | fr | es | tr | ja | zh | ru | ar | hi
      paginate="ltr" // bottom | ltr
      buttonColor="#141414" // pagination button color
      printable // print button visible
      zoomable // zoom in and out button visible
    />
  );
};

export default App;
