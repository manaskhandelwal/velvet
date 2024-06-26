"use client";

import { useEffect, useState } from "react";
import { API } from "../../utils/api";
import { useRouter } from "next/navigation";
import { Header } from "../../module/header";
import { Moment, Profile, User } from "../../module/profile";

export default function ProfilePage() {
  const [user, setUser] = useState<null | User>(null);
  const [moments, setMoments] = useState<null | Moment[]>(null);
  const router = useRouter();

  const getUser = async () => {
    const userRes = await API.get("/user/me");
    setUser(userRes.data);

    const momentsRes = await API.get("/user/moments");
    setMoments(momentsRes.data);
  };

  useEffect(() => {
    const accessToken = localStorage.getItem("access_token");
    if (!accessToken) router.push("/");

    (async () => await getUser())();
  }, [router]);

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
