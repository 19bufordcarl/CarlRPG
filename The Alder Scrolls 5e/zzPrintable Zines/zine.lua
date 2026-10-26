-- Tables stay exactly where they appear in the source
function Table(el)
  el.classes:insert("float")
  el.attributes["latex-placement"] = "H"
  return el
end

-- <!-- pagebreak --> in source becomes \pagebreak in LaTeX
function RawBlock(el)
  if el.format == 'html' and el.text:find('pagebreak', 1, true) then
    return pandoc.RawBlock('latex', '\\pagebreak')
  end
  return el
end

-- Promote "X Spell List" headings to top level
-- (Two triggers: .toplevel class, or a heading ending in "Spell List")
function Header(el)
  if el.classes:includes('toplevel') then
    el.level = 1
    return el
  end
  if el.level == 2 and pandoc.utils.stringify(el.content):match('Spell List$') then
    el.level = 1
  end
  return el
end

-- Remove horizontal rules between spells
function HorizontalRule(el)
  return {}
end