"use client";

import { useState, useEffect } from "react";
import { Header } from "../../../module/header";
import { User, Moment, Profile } from "../../../module/profile";
import { API } from "../../../utils/api";

export default function ProfilePage({
  params,
}: {
  params: { username: string };
}) {
  const [user, setUser] = useState<null | User>(null);
  const [moments, setMoments] = useState<null | Moment[]>(null);

  const getUser = async () => {
    const userRes = await API.get(`/user/p/${params.username}`);
    setUser(userRes.data);

    const momentsRes = await API.get(`/moment/p/${userRes.data.id}`);
    setMoments(momentsRes.data);
  };

  useEffect(() => {
    console.log(params.username);
    (async () => await getUser())();
  }, []);

  if (!user || !moments) {
    return (
      <div>
        <Header />
        <section className={`w-full h-full grid justify-center my-20`}>
          Loading 😁😁😁...
        </section>
      </div>
    );
  }

  return <Profile user={user} moments={moments} />;
}
