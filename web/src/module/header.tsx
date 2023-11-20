"use client";

import { useRouter } from "next/navigation";
import {
  NavigationMenu,
  NavigationMenuList,
  NavigationMenuItem,
  NavigationMenuLink,
  navigationMenuTriggerStyle,
} from "../components/ui/navigation-menu";
import Link from "next/link";
import { Logo } from "../components/logo";
import clsx from "clsx";
import { Wrapper } from "../components/wrapper";
import { Avatar, AvatarImage, AvatarFallback } from "../components/ui/avatar";
import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuItem,
} from "../components/ui/dropdown-menu";
import { useEffect, useState } from "react";
import { API } from "../utils/api";

interface HeaderProps {}

export const Header: React.FC<HeaderProps> = ({}) => {
  const router = useRouter();
  const [profilePhoto, setProfilePhoto] = useState<string | null>(null);
  const [fullName, setFullName] = useState<string | null>(null);

  const getUser = async () => {
    const { data } = await API.get("/user/me");
    setProfilePhoto(data.profile_photo);
    setFullName(data.full_name);
  };

  useEffect(() => {
    (async () => await getUser())();
  }, []);

  return (
    <div className="w-[calc(100vw-20px)] border-b">
      <Wrapper className={`py-4 flex justify-between items-center`}>
        <Link href="/feed">
          <Logo />
        </Link>

        <div className={`flex justify-between items-center gap-10`}>
          <NavigationMenu>
            <NavigationMenuList>
              <NavigationMenuItem>
                <Link href="/feed" passHref>
                  <NavigationMenuLink
                    className={clsx(navigationMenuTriggerStyle(), "mr-6")}
                  >
                    For You
                  </NavigationMenuLink>
                </Link>
              </NavigationMenuItem>
            </NavigationMenuList>
          </NavigationMenu>
          <DropdownMenu>
            <DropdownMenuTrigger className={`outline-none`}>
              <Avatar className={`w-8 h-8 m-auto`}>
                <AvatarImage src={profilePhoto ? profilePhoto : ""} />
                <AvatarFallback>
                  {fullName
                    ? fullName
                        .split(" ")
                        .map((w) => w[0])
                        .join("")
                        .toUpperCase()
                    : "🧑"}
                </AvatarFallback>
              </Avatar>
            </DropdownMenuTrigger>
            <DropdownMenuContent>
              <DropdownMenuLabel>My Account</DropdownMenuLabel>
              <DropdownMenuSeparator />
              <DropdownMenuItem onClick={() => router.push("/profile")}>
                Profile
              </DropdownMenuItem>
              <DropdownMenuItem>Followers</DropdownMenuItem>
              <DropdownMenuItem>Followings</DropdownMenuItem>
              <DropdownMenuItem>Cherishes</DropdownMenuItem>
              <DropdownMenuItem>Notifications</DropdownMenuItem>
              <DropdownMenuItem>Settings</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </Wrapper>
    </div>
  );
};
