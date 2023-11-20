"use client";

import { Label } from "../../../components/ui/label";
import { CenterBox } from "../../../components/center-box";
import { Button } from "../../../components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "../../../components/ui/card";
import { Input } from "../../../components/ui/input";
import { Header } from "../../../module/header";
import { useForm, SubmitHandler } from "react-hook-form";
import { API } from "../../../utils/api";
import { Textarea } from "../../../components/ui/textarea";
import { useRouter } from "next/navigation";

interface IUpdateProfileFormInput {
  profilePhoto: any;
  pronouns: string;
  bio: string;
}

export default function ProfileUpdatePage() {
  const router = useRouter();

  const {
    register,
    handleSubmit,
    formState: { errors },
    setError,
  } = useForm<IUpdateProfileFormInput>();

  const onSubmit: SubmitHandler<IUpdateProfileFormInput> = async (data) => {
    try {
      console.log({ data });

      const file = data.profilePhoto[0];
      const reader = new FileReader();
      reader.readAsBinaryString(file);

      reader.onload = async function () {
        const base64 = btoa(reader.result as string);

        const responce = await API.post("/user/update-profile", {
          profile_photo: `data:image/jpeg;base64,${base64}`,
          pronouns: data.pronouns,
          bio: data.bio,
          private: false,
        });

        if (responce.data.success) {
          router.push("/profile");
        }
      };
    } catch (error: any) {
      const err = error.response.data.detail;
      if (!err) return;
    }
  };

  return (
    <div>
      <Header />
      <section className={`my-20`}>
        <CenterBox>
          <Card>
            <CardHeader>
              <CardTitle className={`text-2xl mb-4 text-center`}>
                Update Profile
              </CardTitle>
              <CardDescription></CardDescription>
            </CardHeader>
            <CardContent>
              <form className="space-y-2" onSubmit={handleSubmit(onSubmit)}>
                <div className={`flex flex-col gap-5 mb-10`}>
                  <div className="space-y-1">
                    <Label htmlFor="profilePhoto">Profile Photo</Label>
                    <Input
                      id="profilePhoto"
                      type="file"
                      className={`text-white`}
                      {...register("profilePhoto")}
                    />
                  </div>

                  <div className="space-y-1">
                    <Label htmlFor="pronouns">Pronouns</Label>
                    <Input
                      id="pronouns"
                      placeholder="he/him"
                      {...register("pronouns")}
                    />
                    {errors.pronouns ? (
                      <p role="alert" className={`text-xs text-red-500`}>
                        {errors.pronouns.message}
                      </p>
                    ) : null}
                  </div>

                  <div className="space-y-1">
                    <Label htmlFor="bio">Bio</Label>
                    <Textarea
                      id="bio"
                      placeholder="Hi, I am xyz..."
                      className={`min-h-[100px]`}
                      {...register("bio")}
                    />
                    {errors.bio ? (
                      <p role="alert" className={`text-xs text-red-500`}>
                        {errors.bio.message}
                      </p>
                    ) : null}
                  </div>
                </div>

                <div className={`flex justify-center`}>
                  <Button>Update Profile</Button>
                </div>
              </form>
            </CardContent>
          </Card>
        </CenterBox>
      </section>
    </div>
  );
}
