import clsx from "clsx";
import "./globals.css";
import type { Metadata } from "next";
import { Bricolage_Grotesque } from "next/font/google";

const bricolageGrotesque = Bricolage_Grotesque({
  subsets: ["latin"],
  weight: ["200", "300", "400", "500", "600", "700", "800"],
});

const description = "A new age positivity spreading social platform.";

export const metadata: Metadata = {
  title: `Velvet: ${description}`,
  description,
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={clsx(bricolageGrotesque.className, "dark")}>
      <body>{children}</body>
    </html>
  );
}
