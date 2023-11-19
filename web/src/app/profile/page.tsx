"use client";

import { useEffect, useState } from "react";
import { API } from "../../utils/api";

export default function Profile() {
  // const [user, setUser] = useState(null);

  const getUser = async () => {
    const response = await API.get("/user/me");
    console.log(response);
  };

  useEffect(() => {
    (async () => await getUser())();
  }, []);

  return <div></div>;
}
