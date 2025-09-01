import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Button } from "@/components/ui/button";
import { useTranslation } from "react-i18next";
import { LuChevronDown } from "react-icons/lu";

type LayoutSelectorProps = {
  layout: string;
  onLayoutChange: (layout: string) => void;
};

const LAYOUTS = ["auto", "2", "3", "4"];

export function LayoutSelector({
  layout,
  onLayoutChange,
}: LayoutSelectorProps) {
  const { t } = useTranslation(["common"]);

  const getLayoutText = (layout: string) => {
    if (layout === "auto") {
      return t("layout.auto", "Auto");
    }
    const count = parseInt(layout);
    return t("layout.columns", "{{count}} Columns", { count });
  };

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" className="flex items-center gap-2">
          <span>{getLayoutText(layout)}</span>
          <LuChevronDown className="h-4 w-4" />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent>
        {LAYOUTS.map((key) => (
          <DropdownMenuItem
            key={key}
            className={layout === key ? "bg-accent" : ""}
            onClick={() => onLayoutChange(key)}
          >
            {getLayoutText(key)}
          </DropdownMenuItem>
        ))}
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
