import { Avatar, AvatarImage, AvatarFallback } from "@radix-ui/react-avatar";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "../components/ui/card";
import { Header } from "./header";
import Image from "next/image";

export interface User {
  profile_photo: string;
  pronouns: string;
  total_following: number;
  bio: string;
  username: string;
  full_name: string;
  total_followers: number;
  private: boolean;
  created_at: string;
  updated_at: string;
}

export interface Moment {
  message: string | null;
  total_cherishes: 0;
  user_id: string;
  id: string;
  updated_at: string;
  private: boolean;
  photo: string | null;
  created_at: string;
}

interface ProfileProps {
  user: User;
  moments: Moment[];
}

export const Profile: React.FC<ProfileProps> = ({ user, moments }) => {
  return (
    <div>
      <Header />
      <section className={` w-full h-full grid justify-center my-20`}>
        <div className={`w-[1000px]`}>
          <div className="flex gap-24">
            <div className={`w-[35%]`}>
              <Card>
                <CardHeader className={`text-center`}>
                  <Avatar className={`w-48 h-48 m-auto`}>
                    <AvatarImage src={user.profile_photo} />
                    <AvatarFallback>
                      {user.full_name
                        .split(" ")
                        .map((w) => w[0])
                        .join("")
                        .toUpperCase()}
                    </AvatarFallback>
                  </Avatar>
                  <CardTitle className={`pt-6 text-3xl`}>
                    {user.full_name}
                  </CardTitle>
                  <CardDescription className={`pt-2`}>
                    {user.pronouns}
                  </CardDescription>
                </CardHeader>
                <CardContent className={`text-zinc-400 leading-7 mt-7`}>
                  {user.bio
                    ? user.bio.split("\n").map((text, i) => (
                        <p key={i} className={`my-3`}>
                          {text}
                        </p>
                      ))
                    : null}
                </CardContent>
                <CardFooter className={`mt-7 flex gap-4`}>
                  <div className={`bg-zinc-900 p-4 rounded-lg text-center`}>
                    <span className={`text-3xl font-bold`}>
                      {user.total_followers}
                    </span>
                    <p className={`text-zinc-500 mt-2`}>Followers</p>
                  </div>
                  <div className={`bg-zinc-900 p-4 rounded-lg text-center`}>
                    <span className={`text-3xl font-bold`}>
                      {user.total_following}
                    </span>
                    <p className={`text-zinc-500 mt-2`}>Following</p>
                  </div>
                </CardFooter>
              </Card>
            </div>
            <div className={`w-[65%]`}>
              <h1 className={`text-4xl font-bold mb-10`}>Your Moments</h1>
              <div className={`flex flex-col gap-8`}>
                {moments.map((m) => {
                  const d = new Date(m.created_at);

                  return (
                    <Card key={m.id}>
                      <CardContent className={`flex gap-10 mt-5`}>
                        <p className={`leading-8 text-lg font-normal`}>
                          {m.message}
                        </p>
                        {m.photo ? (
                          <Image
                            alt={m.message ? m.message : ""}
                            src={m.photo}
                            width={200}
                            height={200}
                          />
                        ) : null}
                      </CardContent>
                      <CardFooter className={`flex justify-between mt-6`}>
                        <p
                          className={`bg-zinc-900 px-4 py-3 rounded-lg flex items-center gap-2`}
                        >
                          <Image
                            alt={"cherish icon"}
                            src={"/cherish.png"}
                            width={20}
                            height={20}
                          />
                          <span className={`font-bold`}>
                            {m.total_cherishes}
                          </span>
                        </p>

                        <p className={`text-sm text-zinc-500`}>
                          Posted On:{" "}
                          <span className={`font-bold`}>
                            {d.getDate()}/{d.getMonth() + 1}/{d.getFullYear()}
                          </span>
                        </p>
                      </CardFooter>
                    </Card>
                  );
                })}
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};
