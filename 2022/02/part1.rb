scores = {
  "X" => 1,
  "Y" => 2,
  "Z" => 3,
}

translation = {
  "A" => "X",
  "B" => "Y",
  "C" => "Z",
}

throws = ["X", "Y", "Z"]

rounds = File.read("strategy.txt").strip().split("\n")

total_score = 0

for round in rounds
  opponent_throw = translation[round.split[0]]
  my_throw = round.split[1]
  total_score += scores[my_throw]
  my_throw_index = throws.find_index(my_throw)
  if throws[my_throw_index - 1] == opponent_throw
    total_score += 6
    next
  elsif my_throw == opponent_throw
    total_score += 3
  end
end

puts "this outcome will yield a total score of #{total_score}"
