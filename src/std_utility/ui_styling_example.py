from ui_styling import StringFormatting
sample_text = "It's a Gym, not a Spa\n"

print(StringFormatting(sample_text)
      .red()
      .bold()
      .italic()
      .underline()
      .strikethrough()
      .append("Terve Nwanne\n")
      .bg_blue()
      .italic()
      .append("Welcome!!!!")
      .underline())

(StringFormatting("Oj Skills")
 .blue().underline().bg_red()
 .append("ifeanyi")
 .green().bold().print())


