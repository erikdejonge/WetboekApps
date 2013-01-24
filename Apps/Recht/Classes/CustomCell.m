

#import "CustomCell.h"


@implementation CustomCell

@synthesize titel ;
@synthesize midtitel ;
@synthesize subtitel ;

-(id) initWithFrame: (CGRect) frame reuseIdentifier: (NSString *) reuseIdentifier
{
  if (self = [super initWithFrame:frame]) {
  }
  return(self) ;
}


-(void) setSelected: (BOOL) selected animated: (BOOL) animated
{
  [super setSelected:selected animated:animated] ;

  // Configure the view for the selected state
}


-(void) dealloc
{
  [super dealloc] ;
}


@end
